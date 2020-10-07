import * as React from "react";
import IconSvg from "../icons-svg/icons";
import { HeaderWrapper, GroupButtons, NavButton, DragWindow } from "./style";

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
    this.setState(
      {
        ipcRenderer: window.require("electron").ipcRenderer,
      },
      () => {
        this.state.ipcRenderer.on(
          "reply-done-training",
          (event: any, args: any) => {
            console.log("HEADER", args);
            this.setState({ loading: false });
          }
        );
      }
    );
  };

  openTrainingMode = () => {
    const { ipcRenderer } = this.state;

    this.setState({ loading: true }, () => {
      ipcRenderer.send("open-training");
    });
  };

  openTreeTrainingMode = () => {
    const { ipcRenderer } = this.state;

    this.setState({ loading: true }, () => {
      ipcRenderer.send("open-training-tree");
    });
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
            <h1>Aprendizado de máquina</h1>
          </DragWindow>
          <NavButton
            onClick={this.openTrainingMode}
            disabled={this.state.loading}
            useMinWidth={true}
          >
            {!this.state.loading ? "Treinar Naive Bayes" : "Em treinamento..."}
          </NavButton>
          <NavButton
            onClick={this.openTreeTrainingMode}
            disabled={this.state.loading}
            useMinWidth={true}
          >
            {!this.state.loading
              ? "Treinar árvore de decisão"
              : "Em treinamento..."}
          </NavButton>

          <NavButton
            style={{ color: "orange", background: "none" }}
            onClick={() => window.close()}
          >
            Sair da aplicação
          </NavButton>
        </GroupButtons>
      </HeaderWrapper>
    );
  }
}
