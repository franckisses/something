#6. Modules
如果你终止了python解释器的执行，然后在继续执行，你之前定义的一个函数变量就会没用了。因此，你需要写一个可移植性比较高的代码，你最好用编辑器写一个文件然后在去运行它，就像写一个脚本一样。如果你的代码特别长的话，你最好把它写成几个文件，这样的话，以后维护起来会好一点，你也会遇到需要一个处理函数来操作你之前写的代码。<br>
为了能做到这些。python有一种方法可以做到。put definitions in a file and use them in a script or in an interactive instance of the interpreter.这样的文件叫做模块。定义的这个模块可以导入到其他的模块，或者是主模块中。<br>
模块是一个文件，包含python的定义和声明，文件名就是模块名。以.py为后缀结尾的。在文件的内部，模块的名字是一个全局变量__name__来获取，来吧试试吧：

	# Fibonacci numbers module

	def fib(n):    # write Fibonacci series up to n
	    a, b = 0, 1
	    while a < n:
	        print(a, end=' ')
	        a, b = b, a+b
	    print()
	
	def fib2(n):   # return Fibonacci series up to n
	    result = []
	    a, b = 0, 1
	    while a < n:
	        result.append(a)
	        a, b = b, a+b
	    return result
现在打开任意一个python解释器导入这个模块，然后输入这个指令试试吧：

	>>> import fibo
this does not enter the names of the functions defined in fibo directly in the current symbol table,如果在这里只输入模块的名字fibo的话，通过模块名你也可以调用这个函数：

	>>> fibo.fib(1000)
	0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
	>>> fibo.fib2(100)
	[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	>>> fibo.__name__
	'fibo'
如果你经常用这个模块的话，你可以对其进行赋值。

	>>> fib = fibo.fib
	>>> fib(500)
	0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
##6.1 详解模块
一个模块包含一个可以执行的语句和定义的函数，这些语句做的事情就是初始化这个模块，这些执行的情况是当被导入时候第一次执行这些语句.<br>
Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables. On the other hand, if you know what you are doing you can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.<br>
在模块里边可以导入其他的模块，It is customary but not required to place all import statements at the beginning of a module (or script, for that matter). The imported module names are placed in the importing module’s global symbol table.<br>
这里有几种不同的导入模块的方式可以参考

	>>> from fibo import fib, fib2
	>>> fib(500)
	0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
This does not introduce the module name from which the imports are taken in the local symbol table (so in the example, fibo is not defined).<br>
还有一种方法就是导入模块的所有定义的方法：

	>>> from fibo import *
	>>> fib(500)
	0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
This imports all names except those beginning with an underscore (_). In most cases Python programmers do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.

Note that in general the practice of importing * from a module or package is frowned upon, since it often causes poorly readable code. However, it is okay to use it to save typing in interactive sessions.

If the module name is followed by as, then the name following as is bound directly to the imported module.

	>>> import fibo as fib
	>>> fib.fib(500)
	0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
这是一个有效的导入模块的方法，import fibo。with the only difference of it being available as fib.

通过from的方式也可以导入，达到相同的效果。
	
	>>> from fibo import fib as fibonacci
	>>> fibonacci(500)
	0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
NOTE:为了效率，一个模块一般在导入第一次的时候就被编译了，如果模块的内容发生了改变，你就也要重启编辑器，或者通过importlib。reload（）方法来重新加载，例如：import.importlib ; import.reload(modulename);
##6.1.1 执行脚本
当你在命令行执行python文件时：

	>>> python fibo.py <arguement>
在模块里边的代码会被执行一遍，如果你导入的话。但是如果出现__name__==__main__的话。意味着这句话要加在你的代码的最后一行。

	if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
你可以像执行脚本一样去执行python 的文件，因为在命令行执行的话，就相当于主文件：
	
	$ python fibo.py 50
	0 1 1 2 3 5 8 13 21 34
如果模块被导入了，但是代码没有运行的话：
	
	>>>import fibo
	>>>
这个一般是用来给用户提供一个比较方便的调用接口，或者是在测试的时候。
##6.1.2 模块的搜索路径
当模块的导入路径被定义之后，解释器回在内建的模块中搜索需要导入的模块，如果没有找到的话，然后继续在目录或者列表中搜索文件名字叫做spam.py的文件，把文件名用作变量通过sys.path（）

- 目录包含着输入的脚本
- PYTHONPATH
- 默认的安装路径

Note：在文件系统中，支持者文件的链接，the directory containing the input script is calculated after the symlink is followed. In other words the directory containing the symlink is not added to the module search path.
在初始化之后，python的程序能够修改文件的路径，The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path.This means that scripts in that directory will be loaded instead of modules of the same name in the library directory.this is an error unless the replacement is intended .到标准库模块那一章可以看到更多的详细信息。
##6.1.3 文件的编译
为了加快模块的加在，python已经将所有的模块已经加在一遍了，在__pychche__目录中的module.version.pyc中。在哪里将所有的模块已经编译成为计算机编译的版本了。他也包括了python的版本文件，举个例子：在CPython 3.3的已经编译的版本就存放在 __pycache__/spam.cpython-33.pyc，这种命名的方法适用于不同的版本下有不同的编译文件。<br>
Python checks the modification date of the source against the compiled version to see if it’s out of date and needs to be recompiled. This is a completely automatic process. Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures.

Python does not check the cache in two circumstances. First, it always recompiles and does not store the result for the module that’s loaded directly from the command line. Second, it does not check the cache if there is no source module. To support a non-source (compiled only) distribution, the compiled module must be in the source directory, and there must not be a source module.

Some tips for experts:

	You can use the -O or -OO switches on the Python command to reduce the size of a compiled module. The -O switch removes assert statements, the -OO switch removes both assert statements and __doc__ strings. Since some programs may rely on having these available, you should only use this option if you know what you’re doing. “Optimized” modules have an opt- tag and are usually smaller. Future releases may change the effects of optimization.
	A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file; the only thing that’s faster about .pyc files is the speed with which they are loaded.
	The module compileall can create .pyc files for all modules in a directory.
	There is more detail on this process, including a flow chart of the decisions, in PEP 3147.
##6.2  标准模块
python有一列的标准模块，在不同的文档中都有描述，python库参考。一些模块就存在于python的解释器中，these provide access to operations that are not part of the core of the language but are nevertheless built in, either for efficiency or to provide access to operating system primitives such as system calls. The set of such modules is a configuration option which also depends on the underlying platform. For example, the winreg module is only provided on Windows systems. One particular module deserves some attention: sys, which is built into every Python interpreter. The variables sys.ps1 and sys.ps2 define the strings used as primary and secondary prompts:

	>>> import sys
	>>> sys.ps1
	'>>> '
	>>> sys.ps2
	'... '
	>>> sys.ps1 = 'C> '
	C> print('Yuck!')
	Yuck!
	C>
These two variables are only defined if the interpreter is in interactive mode.

The variable sys.path is a list of strings that determines the interpreter’s search path for modules. It is initialized to a default path taken from the environment variable PYTHONPATH, or from a built-in default if PYTHONPATH is not set. You can modify it using standard list operations:

	>>>import sys
	>>>sys.path.append('/ufs/guido/python')
##6.3 函数dir（）
内减函数dir（）用来查找模块里边被定义的方法，返回值是定义方法的列表。

	>>> import fibo, sys
	>>> dir(fibo)
	['__name__', 'fib', 'fib2']
	>>> dir(sys)  
	['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
	 '__package__', '__stderr__', '__stdin__', '__stdout__',
	 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
	 '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
	 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
	 'call_tracing', 'callstats', 'copyright', 'displayhook',
	 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
	 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
	 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
	 'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
	 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
	 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
	 'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
	 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
	 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
	 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
	 'thread_info', 'version', 'version_info', 'warnoptions']
如果没参数的话，dir（）返回的是当前被定义的内容。
    
	>>> a = [1, 2, 3, 4, 5]
	>>> import fibo
	>>> fib = fibo.fib
	>>> dir()
	['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
注意：也会返回所有的对象类型，变量，模块，函数等<br>
dir()不会列出所有的内建函数和变量，如果想看获得的话，他们都在标准模块中 builtins。

	>>> import builtins
	>>> dir(builtins)  
	['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
	 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
	 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
	 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
	 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
	 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
	 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
	 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
	 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
	 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
	 'NotImplementedError', 'OSError', 'OverflowError',
	 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
	 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
	 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
	 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
	 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
	 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
	 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
	 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
	 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
	 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
	 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
	 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
	 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
	 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
	 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
	 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
	 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
	 'zip']
##6.4 包
包就是python中的结构化的模块。例如：For example, the module name A.B designates a submodule named B in a package named A. Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other’s module names.

Suppose you want to design a collection of modules (a “package”) for the uniform handling of sound files and sound data. There are many different sound file formats (usually recognized by their extension, for example: .wav, .aiff, .au), so you may need to create and maintain a growing collection of modules for the conversion between the various file formats. There are also many different operations you might want to perform on sound data (such as mixing, adding echo, applying an equalizer function, creating an artificial stereo effect), so in addition you will be writing a never-ending stream of modules to perform these operations. Here’s a possible structure for your package (expressed in terms of a hierarchical filesystem):

	sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
当导入一个模块之后，python就开始通过sys.path方法开始在子目录中搜寻。

The __init__.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable, described later.

Users of the package can import individual modules from the package,for example:

	import sound.effect.echo
这个可以导入子模块sound.effect.echo 但必须写的是全名，不能缩写。

	sound.effects.echo.echofilter(input,output,delay=0.7,atten=4)
另一种可供选择的方法是：
	
	from sound.effects import echo
这样也可以导入模块，不用将包前置，具体的示例如下：

	echo.echofilter(input,output,delay=0.7,atten=4)
还有另外一种导入模块的方法是：
	
	from sound.effect.echo import echofilter
这种导入模块的方式是可以将子模块直接导入，并且这种方法可以使函数echofilter直接可用：

	echifilter（input，output，delay=0.7,atten=4）
注意：当使用from package import item的时候，这个item可以是这个包的子模块，也可以是已经被定义的另一个包，函数，类，或者变量，import 语句首先去检查被导入的包是否被定义，如果有的话，就会尝试去加载这个包，如果没有的话，此时就会出现导入异常的错误。
##6.4.1 导入
当用户写下这句：‘from sound.effects import *’,会发生什么呢？一种想法就是：one would hope that this somehow goes out to the filesystem, finds which submodules are present in the package, and imports them all. This could take a long time and importing sub-modules might have unwanted side-effects that should only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the package. The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__, it is taken to be the list of module names that should be imported when from package import * is encountered. It is up to the package author to keep this list up-to-date when a new version of the package is released. Package authors may also decide not to support it, if they don’t see a use for importing * from their package. For example, the file sound/effects/__init__.py could contain the following code:

	__all__ = ['echo','surround','reverse']
这就意味这通过 from sound.effects import * 将会导入已经命名好的三个模块。<br>
the statement from sound.effects import * does not import all submodules from the package sound.effects into the current namespace; it only ensures that the package sound.effects has been imported (possibly running any initialization code in __init__.py) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by __init__.py. It also includes any submodules of the package that were explicitly loaded by previous import statements. Consider this code:

	import sound.effect.echo
	import sound.effects.surround
	from sound.effects import *
在这个例子中，echo和surround模块，被导入到当前的命名空间了。当使用from ... import语句执行的时候，他们就在这个包里边已经被定义了。

Although certain modules are designed to export only names that follow certain patterns when you use import *, it is still considered bad practice in production code.

Remember, there is nothing wrong with using from Package import specific_submodule! In fact, this is the recommended notation unless the importing module needs to use submodules with the same name from different packages.
##6.4.2 内部模块的引用
When packages are structured into subpackages (as with the sound package in the example), you can use absolute imports to refer to submodules of siblings packages. For example, if the module sound.filters.vocoder needs to use the echo module in the sound.effects package, it can use from sound.effects import echo.

You can also write relative imports, with the from module import name form of import statement. These imports use leading dots to indicate the current and parent packages involved in the relative import. From the surround module for example, you might use:

	from ... import echo
	from ... import formats
	from .. filters import equalizer
Note that relative imports are based on the name of the current module. Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application must always use absolute imports.
##6.4.3. Packages in Multiple Directories
Packages support one more special attribute, __path__. This is initialized to be a list containing the name of the directory holding the package’s __init__.py before the code in that file is executed. This variable can be modified; doing so affects future searches for modules and subpackages contained in the package.

While this feature is not often needed, it can be used to extend the set of modules found in a package.
