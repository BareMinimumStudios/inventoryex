
plugins {
	kotlin("jvm") version libs.versions.kotlin
	alias(libs.plugins.cloche)
}

group = "xyz.naomieow.invex"
version = "1.0.1"

repositories {
	cloche.librariesMinecraft()

	mavenCentral()

	cloche {
		main()
		mavenFabric()
	}

	maven("https://maven.nucleoid.xyz")
	maven("https://maven.terraformersmc.com/")
	maven("https://maven.ladysnake.org/releases")
	maven("https://maven.wispforest.io/releases")
	maven("https://maven.shedaniel.me/")
}

cloche {
	metadata {
		modId = "invex"
		name = "Inventory EX"
		description = "Server-side inventory and Ender Chest viewer with offline player, Trinkets, and Accessories support."
		license = "BML-1.0"

		author {
			name = "naomieow"
		}

		author {
			name = "pokesmells"
		}

		url = "https://github.com/BareMinimumStudios/invex"
		sources = "https://github.com/BareMinimumStudios/invex"
		issues = "https://github.com/BareMinimumStudios/invex/issues"

		icon = "assets/invex/icon.png"
	}

	common {
		mappings {
			official()
		}

		dependencies {
			modImplementation(libs.fabric.kotlin)
		}
	}

	fabric("1.20.1") {
		minecraftVersion = "1.20.1"
		loaderVersion = libs.versions.fabric.loader

		runs {
			server()
		}

		dependencies {
			fabricApi(libs.versions.fabric.api.get1201())
			modImplementation(libs.sgui.get1201())
			include(libs.sgui.get1201())
			modImplementation(libs.permissionsapi.get1201())
			include(libs.permissionsapi.get1201())

			modCompileOnly(libs.trinkets.get1201())
			modCompileOnly(libs.accessories.get1201())
		}

		metadata {
			dependencies {
				dependency {
					modId = "fabric-api"
					version(libs.versions.fabric.api.get1201().get())
				}
				dependency {
					modId = "fabric-language-kotlin"
					version(libs.versions.fabric.kotlin.get())
				}
			}

			entrypoint("main") {
				adapter = "kotlin"
				value = "xyz.naomieow.invex.InvEx"
			}
		}
	}

	fabric("1.21.1") {
		minecraftVersion = "1.21.1"
		loaderVersion = libs.versions.fabric.loader

		runs {
			server()
		}

		dependencies {
			fabricApi(libs.versions.fabric.api.get1211())
			modImplementation(libs.sgui.get1211())
			include(libs.sgui.get1211())
			modImplementation(libs.permissionsapi.get1211())
			include(libs.permissionsapi.get1211())

			modCompileOnly(libs.trinkets.get1211())
			modCompileOnly(libs.accessories.get1211())
		}

		metadata {
			dependencies {
				dependency {
					modId = "fabric-api"
					version(libs.versions.fabric.api.get1211().get())
				}
				dependency {
					modId = "fabric-language-kotlin"
					version(libs.versions.fabric.kotlin.get())
				}
			}

			entrypoint("main") {
				adapter = "kotlin"
				value = "xyz.naomieow.invex.InvEx"
			}
		}
	}
}

kotlin {
	compilerOptions {
		freeCompilerArgs = listOf("-Xmulti-platform", "-Xno-check-actual", "-Xexpect-actual-classes")
	}
}

// Cloche remapping resolves these artifacts while preparing dependency access wideners.
for (target in listOf("1201", "1211")) {
    tasks.named("accessWiden${target}CommonMinecraft") {
        dependsOn("generate${target}MappingsArtifact")
    }
}

// Keep each release restricted to its tested Minecraft branch.
for ((target, minecraft, java) in listOf(Triple("1201", "1.20.1", "17"), Triple("1211", "1.21.1", "21"))) {
    tasks.named("generate${target}ModJson") {
        doLast {
            for (file in outputs.files.asFileTree.files.filter { it.name == "fabric.mod.json" }) {
                @Suppress("UNCHECKED_CAST")
                val metadata = groovy.json.JsonSlurper().parse(file) as MutableMap<String, Any>
                @Suppress("UNCHECKED_CAST")
                val dependencies = metadata["depends"] as MutableMap<String, Any>
                dependencies["minecraft"] = "~$minecraft"
                dependencies["java"] = ">=$java"
                metadata["environment"] = "server"
                file.writeText(groovy.json.JsonOutput.prettyPrint(groovy.json.JsonOutput.toJson(metadata)))
            }
        }
    }
}
