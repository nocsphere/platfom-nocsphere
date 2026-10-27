from SCons.Script import Import

Import("env")

board_config = env.BoardConfig()

machine_flags = [
    "-march=%s" % board_config.get("build.march"),
    "-mabi=%s" % board_config.get("build.mabi"),
    "-mcmodel=%s" % board_config.get("build.mcmodel")
]

env.Append(
    ASFLAGS=machine_flags,

    ASPPFLAGS=[
        "-x", "assembler-with-cpp",
    ],

    CCFLAGS=machine_flags + [
        "-O0",
        "-Wall",  # show warnings
    ],

    LINKFLAGS=machine_flags + [
        "-ffunction-sections",
        "-fdata-sections",
        "--specs=nano.specs",
        "-Wl,--no-warn-rwx-segments",
        "-Wl,--gc-sections"
    ],

    LIBS=[
        "c"
    ],
)
