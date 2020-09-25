import * as React from 'react';
import { HeaderWrapper, NavButton } from './style';

export interface IHeaderProps {}

export interface IHeaderState {}

export default class Header extends React.Component<
  IHeaderProps,
  IHeaderState
> {
  private ipcRenderer?: any;

  constructor(props: IHeaderProps) {
    super(props);
    this.state = {};
  }

  componentDidMount() {
    if (!this.ipcRenderer) {
      this.initializeIpcRenderer();
    }
  }

  initializeIpcRenderer = () => {
    if (!window || !window.process || !window.require) {
      throw new Error(`Unable to require renderer process`);
    }
    this.ipcRenderer = window.require('electron').ipcRenderer;
  };

  openTrainingMode = () => {
    this.ipcRenderer.send('open-training', 'ping');
  };

  exitApp = () => {
    this.ipcRenderer.send('close-program', 'ping');
  };

  public render() {
    return (
      <HeaderWrapper>
        <NavButton onClick={() => this.openTrainingMode()}>
          Treinamento
        </NavButton>
        <NavButton onClick={() => this.exitApp()}>Sair</NavButton>
      </HeaderWrapper>
    );
  }
}
