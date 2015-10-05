

	checkout nach LinuxMain/TTCN-3_Example


cd libcwebui/LinuxMain
git clone https://github.com/lordrasmus/TTCN-3-Test.git TTCN-3_Example


	Webserver Main Config



WebserverAddFileDir("TTCN-3_Example", "TTCN-3_Example");

WebserverLoadPyPlugin( "TTCN-3_Example/ttcn3.py");

WebserverConfigSetInt( "use_csp",0);


	menu.inc


<tr><td><a class={get:render;"mp18_class"} href={b:link_std}/TTCN-3_Example/index.html>TTCN-3 API</a>
