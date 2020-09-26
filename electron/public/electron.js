const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const fs = require('fs');
const isDev = require('electron-is-dev');
const _dirname = '';
const { PythonShell } = require('python-shell');

class Main {
  init() {
    app.on('ready', this.createWindow);
    app.on('window-all-closed', this.onWindowAllClosed);
    app.on('activate', this.onActivate);
    this.listenerActions();
  }

  listenerActions() {
    //Training Action
    ipcMain.on('open-training', (event, args) => {
      let pyshell = new PythonShell('open_training.py', {
        mode: 'text',
        pythonPath: 'python3',
        scriptPath: path.join(__dirname, '../../python'),
      });

      pyshell.on('message', function (results) {
        console.log(results);
        event.reply('python-events', results);
      });
    });

    ipcMain.on('classify-image', (event, args) => {
      const { data } = args;

      let pyshell = new PythonShell('classify_image.py', {
        mode: 'text',
        pythonPath: 'python3',
        args: [data],
        scriptPath: path.join(__dirname, '../../python'),
      });

      pyshell.on('message', function (results) {
        event.reply('python-events', results);
      });
    });

    //Exit Action
    ipcMain.on('close-program', (event, arg) => {
      console.log('CLOSE', event);
      app.quit();
    });
  }

  onWindowAllClosed() {
    if (process.platform !== 'darwin') {
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
      backgroundColor: '#282c34',
      webPreferences: {
        nodeIntegration: true,
        webSecurity: false,
        allowRunningInsecureContent: true,
      },
    });

    win.loadURL(
      isDev
        ? 'http://localhost:3000'
        : `file://${path.join(_dirname, '../build/index.html')}`
    );

    win.once('ready-to-show', () => {
      win.show();
    });
    // win.webContents.openDevTools()
  }
}

new Main().init();
