function ejecutarPython() {
    var spawn = require("child_process").spawn;
    var proceso = spawn('python', ['./python_rev_v1.py']);
    proceso.stdout.on('data', function (data) {
        console.log(data.toString());
    });
}
