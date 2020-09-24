const { app, BrowserWindow, ipcMain } = require("electron");
const path = require("path");
const fs = require("fs");
const isDev = require("electron-is-dev");
const _dirname = "";

class Main {
  init() {
    app.on("ready", this.createWindow);
    app.on("window-all-closed", this.onWindowAllClosed);
    app.on("activate", this.onActivate);
  }

  listenerActions() {
    //Training Action
    ipcMain.on("open-training", (event, arg) => {
      console.log("Training", event);
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
      height: 800,
      frame: true,
      show: true,
      // titleBarStyle: "hidden ",
      transparent: true,
      backgroundColor: "#282c34",
      webPreferences: {
        nodeIntegration: true
      }
    });

    win.loadURL(
      isDev
        ? "http://localhost:3000"
        : `file://${path.join(_dirname, "../build/index.html")}`
    );

    win.once("ready-to-show", () => {
      win.show();
    });
    // win.webContents.openDevTools()
  }
}

new Main().init();