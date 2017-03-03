from conans import ConanFile
import os
from conans.tools import download
from conans.tools import unzip
from conans import CMake


class GlewConan(ConanFile):
    name = "glew"
    version = "2.0.0"
    ZIP_FOLDER_NAME = "glew-%s" % version
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports = ["CMakeLists.txt", "FindGLEW.cmake"]
    url="http://github.com/ckanibal/conan-glew"
    license="https://github.com/nigels-com/glew/blob/master/LICENSE.txt"
    
    def source(self):
        zip_name = "glew-%s.zip" % self.version
        url = "https://github.com/nigels-com/glew/releases/download/glew-%s/%s" % (self.version, zip_name)
        download(url, zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        cmake = CMake(self.settings)
        msdos_shell = (self.settings.os == "Windows")
        cd_build = "cd %s/build" % self.ZIP_FOLDER_NAME
        self.run('%s && cmake ./cmake %s' % (cd_build, cmake.command_line))
        self.run("%s && cmake --build . %s" % (cd_build, cmake.build_config))

    def package(self):
		# Copy FindGLEW.cmake to package
        self.copy("FindGLEW.cmake", ".", ".")
	
        # Copying headers
        self.copy(pattern="*.h", dst="include", src="%s/include" % self.ZIP_FOLDER_NAME, keep_path=True)

        # Copying static and dynamic libs
        self.copy(pattern="*.a", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src=".", keep_path=False)
        self.copy(pattern="*.so", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dylib*", dst="lib", src=".", keep_path=False)      
        
        # Copying debug symbols
        if self.settings.compiler == "Visual Studio":
            self.copy(pattern="*.pdb", dst="lib", src=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['libglew32']
        if self.options.shared:
            self.cpp_info.defines = ['GLEW_BUILD']
        else:
            self.cpp_info.defines = ['GLEW_STATIC']
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")