import * as React from "react";
import IconSvg from "../icons-svg/icons";
import { HeaderWrapper, GroupButtons, NavButton, DragWindow } from "./style";

export interface IHeaderProps { }

export interface IHeaderState {
  ipcRenderer?: any;
  loading: boolean;
  classifType: string;
  learning_rate: number;
  trainning_time: number;
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
      classifType: "",
      learning_rate: 0.01,
      trainning_time: 1
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
    this.setState(
      {
        ipcRenderer: window.require("electron").ipcRenderer,
      },
      () => {

      }
    );
  };

  openTrainingMode = () => {
    const { ipcRenderer, learning_rate, trainning_time } = this.state;

    this.setState(
      { classifType: "Áudio", loading: true },
      () => {
        let data = [
          'training',
          learning_rate,
          trainning_time
        ];

        ipcRenderer.send("open-training", { data: data });
      }
    );
  };

  exitApp = () => {
    const { ipcRenderer } = this.state;
    ipcRenderer.send("close-program", "ping");
  };

  public render() {
    return (
      <HeaderWrapper>
        <GroupButtons>
          <DragWindow>
            <h1>Aprendizado de Máquina</h1>
          </DragWindow>

          <NavButton
            // style={{ color: "orange", background: "none" }}
            onClick={() => window.close()}
          >
            Sair da aplicação
          </NavButton>
        </GroupButtons>
      </HeaderWrapper>
    );
  }
}
