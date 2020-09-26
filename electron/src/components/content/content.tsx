import * as React from "react";
import Feature from "../Feature";
import ImageSelector from "../image-selector/image-selector";

import {
  ContentWrapper,
  LeftContent,
  RightContent,
  Btn,
  DisableBtn,
  MessageInfo,
  Image,
} from "./style";

export interface IContentProps {}

export interface IContentState {
  ipcRenderer: any;
  image?: { path?: string; preview?: any };
  confusionMatrix?: string;
  loading: boolean;
}

export default class Content extends React.Component<
  IContentProps,
  IContentState
> {
  constructor(props: IContentProps) {
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
      ipcRenderer: window.require("electron").ipcRenderer,
      loading: false,
    });
  };

  handleImage = (image: object) => {
    console.log("SELECTED-IMAGE", image);
    this.setState({ image });
  };

  classifyAction = () => {
    const { ipcRenderer, image } = this.state;

    if (typeof image == "object") {
      const _this = this;
      this.setState({ loading: true }, () => {
        ipcRenderer.send("classify-image", { data: image.path });
        ipcRenderer.on("python-events", (event: any, args: any) => {
          console.log("args - return ", args);

          if (args.indexOf("data:image")) {
            _this.setState({ loading: false, confusionMatrix: args });
          }
        });
      });
    }
  };

  public render() {
    const { image, loading, confusionMatrix } = this.state;
    return (
      <ContentWrapper>
        <LeftContent>
          <ImageSelector changeImage={this.handleImage} />
          {image ? (
            <Btn onClick={() => this.classifyAction()}>Classificar</Btn>
          ) : (
            <DisableBtn>Classificar</DisableBtn>
          )}

          {loading && !confusionMatrix ? (
            <MessageInfo>Processando imagem...</MessageInfo>
          ) : (
            <Image src={confusionMatrix} />
          )}
        </LeftContent>
        <RightContent>
          <Feature />
        </RightContent>
      </ContentWrapper>
    );
  }
}
