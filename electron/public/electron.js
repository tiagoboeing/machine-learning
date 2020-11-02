const { app, BrowserWindow, ipcMain } = require("electron");
const path = require("path");
const isDev = require("electron-is-dev");
const { PythonShell } = require("python-shell");
let _dirname = path.resolve(path.dirname(""));
// import installExtension, { REDUX_DEVTOOLS } from "electron-devtools-installer";
// Or if you can not use ES6 imports
const {
  default: installExtension,
  REACT_DEVELOPER_TOOLS,
  REDUX_DEVTOOLS,
  REACT_PERF,
} = require("electron-devtools-installer");

class Main {
  init() {
    app.on("ready", this.createWindow);
    app.on("window-all-closed", this.onWindowAllClosed);
    app.on("activate", this.onActivate);
    app.whenReady().then(() => {
      installExtension(REACT_DEVELOPER_TOOLS)
        .then((name) => console.log(`Added Extension:  ${name}`))
        .catch((err) => console.log("An error occurred: ", err));

      installExtension(REDUX_DEVTOOLS)
        .then((name) => console.log(`Added Extension:  ${name}`))
        .catch((err) => console.log("An error occurred: ", err));

      installExtension(REACT_PERF)
        .then((name) => console.log(`Added Extension:  ${name}`))
        .catch((err) => console.log("An error occurred: ", err));
    });
    this.listenerActions();
  }

  listenerActions() {
    //Training Action
    ipcMain.on("open-training", (event, args) => {
      const { data } = args;

      let pyshell = new PythonShell("classify_audio.py", {
        mode: "text",
        pythonPath: "python",
        args: data,
        scriptPath: path.join(__dirname, "../../python"),
      });

      pyshell.on("message", function (results) {
        console.log(results);
        event.reply("python-training", results);
      });
    });

    ipcMain.on("classify-audio", (event, args) => {
      const { data } = args;

      console.log(data);

      let pyshell = new PythonShell("classify_audio.py", {
        mode: "text",
        pythonPath: "python",
        args: data,
        scriptPath: path.join(__dirname, "../../python"),
      });

      pyshell.on("message", function (results) {
        console.log(results);
        event.reply("python-events", results);
      });
    });

    //Done training
    ipcMain.on("done-training", (event, arg) => {
      event.reply("reply-done-training", "done");
    });

    //Exit Action
    ipcMain.on("close-program", (event, arg) => {
      console.log("CLOSE", event);
      app.quit();
    });
  }

  onWindowAllClosed() {
    if (process.platform !== "darwin") {
      app.quit();
    }
  }

  onActivate() {
    if (!this.mainWindow) {
      this.createWindow();
    }
  }

  createWindow() {
    // Cria uma janela de navegação.
    const win = new BrowserWindow({
      width: 1200,
      height: 900,
      frame: false,
      show: true,
      titleBarStyle: "customButtonsOnHover",
      transparent: true,
      backgroundColor: "#282c34",
      webPreferences: {
        nodeIntegration: true,
        webSecurity: false,
        allowRunningInsecureContent: true,
      },
    });

    win.loadURL(
      isDev
        ? "http://localhost:3000"
        : `file://${path.join(_dirname, "/index.html")}`
    );

    win.once("ready-to-show", () => {
      win.show();
    });
    // win.webContents.openDevTools()
  }
}

new Main().init();
