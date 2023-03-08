function ejecutarPython() {
    var spawn = require("child_process").spawn;
    var proceso = spawn('python', ['./prueba.py']);
    proceso.stdout.on('data', function (data) {
        console.log(data.toString());
    });
}
