import * as React from 'react';
import IconSvg from '../icons-svg/icons';
import { HeaderWrapper, GroupButtons, NavButton } from './style';

export interface IHeaderProps {}

export interface IHeaderState {
  ipcRenderer?: any;
  loading: boolean;
}

export default class Header extends React.Component<
  IHeaderProps,
  IHeaderState
> {
  private ipcRenderer?: any;

  constructor(props: IHeaderProps) {
    super(props);

    this.state = {
      ipcRenderer: null,
      loading: false,
    };
  }

  componentDidMount() {
    if (!this.state.ipcRenderer) {
      this.initializeIpcRenderer();
    }
  }

  initializeIpcRenderer = () => {
    if (!window || !window.process || !window.require) {
      throw new Error(`Unable to require renderer process`);
    }
    this.setState({
      ipcRenderer: window.require('electron').ipcRenderer,
    });
  };

  openTrainingMode = () => {
    const { ipcRenderer } = this.state;
    const _this = this;

    this.setState({ loading: true }, () => {
      ipcRenderer.send('open-training');

      ipcRenderer.on('python-events', (event: any, args: any) => {
        if (_this.isJson(args)) {
          let json = JSON.parse(args);

          if (Object.keys(json)[0] === 'uri') {
            console.log('matrix de confusão ' + json.uri);
          }
        }

        _this.setState({ loading: false });
      });
    });
  };

  isJson = (str: string) => {
    try {
      JSON.parse(str);
    } catch (error) {
      return false;
    }

    return true;
  };

  exitApp = () => {
    this.ipcRenderer.send('close-program', 'ping');
  };

  public render() {
    return (
      <HeaderWrapper>
        <GroupButtons>
          <NavButton onClick={() => this.openTrainingMode()}>
            Executar Treinamento
          </NavButton>
        </GroupButtons>
        <NavButton onClick={() => this.exitApp()}>
          Sair <IconSvg icon="exit" color="#61dafb" />{' '}
        </NavButton>
      </HeaderWrapper>
    );
  }
}
