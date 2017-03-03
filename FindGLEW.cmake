#=============================================================================
# Copyright 2001-2011 Kitware, Inc.
#
# Distributed under the OSI-approved BSD License (the "License");
# see accompanying file Copyright.txt for details.
#
# This software is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the License for more information.
#=============================================================================
# (To distribute this file outside of CMake, substitute the full
#  License text for the above reference.)

find_path(GLEW_INCLUDE_DIR GL/glew.h PATHS ${CONAN_INCLUDE_DIRS_GLEW})
find_library(GLEW_LIBRARY NAMES ${CONAN_LIBS_GLEW} PATHS ${CONAN_LIB_DIRS_GLEW})

MESSAGE("** GLEW ALREADY FOUND BY CONAN!")
SET(GLEW_FOUND TRUE)
MESSAGE("** FOUND GLEW:  ${GLEW_LIBRARY}")
MESSAGE("** FOUND GLEW INCLUDE:  ${GLEW_INCLUDE_DIR}")

set(GLEW_INCLUDE_DIRS ${GLEW_INCLUDE_DIR})
set(GLEW_LIBRARIES ${GLEW_LIBRARY})

mark_as_advanced(GLEW_LIBRARY GLEW_INCLUDE_DIR)