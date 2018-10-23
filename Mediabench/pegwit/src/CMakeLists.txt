
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DLITTLE_ENDIAN")

add_executable(pegwit pegwit.c ec_crypt.c ec_curve.c ec_field.c ec_param.c ec_vlong.c square.c sqcts.c sha1.c binasc.c)
