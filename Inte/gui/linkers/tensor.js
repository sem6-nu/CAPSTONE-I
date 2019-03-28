 function detect_object(){

    document.getElementById("detect").value = "Hang on .."
    var python = require("python-shell")
    var path = require("path")

        var options = {
            scriptPath : path.join(__dirname, '/../engine/object_detection'),
            pythonPath : '/Library/Frameworks/Python.framework/Versions/3.7/bin/python3'
        }

        var detect = new python("test.py", options);

        detect.end(function(err, code, message) {
            document.getElementById("detect").value = "Detect Objects"
        })
 }