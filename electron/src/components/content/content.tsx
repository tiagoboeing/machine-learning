import * as React from 'react';
import Feature from '../Feature';
import ImageSelector from '../image-selector/image-selector';

import {
  ContentWrapper,
  LeftContent,
  RightContent,
  Btn,
  DisableBtn,
  MessageInfo,
  Image,
} from './style';

export interface IContentProps {}

export interface IContentState {
  ipcRenderer: any;
  image?: { path?: string; preview?: any };
  confusionMatrix?: string;
  features?: [];
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
    this.setState(
      {
        ipcRenderer: window.require('electron').ipcRenderer,
        loading: false,
      },
      () => {
        this.state.ipcRenderer.on('python-events', (event: any, args: any) => {
          if (this.isJson(args)) {
            let jsonData = JSON.parse(args);

            if (Object.keys(jsonData)[0] === 'uri') {
              console.log('matrix de confusão ' + jsonData.uri);
              this.setState({ confusionMatrix: jsonData.uri });
            }
          }
        });
      }
    );
  };

  handleImage = (image: object) => {
    console.log('SELECTED-IMAGE', image);
    this.setState({ image });
  };

  classifyAction = () => {
    const { ipcRenderer, image } = this.state;

    if (typeof image == 'object') {
      const _this = this;
      this.setState(
        { loading: true, confusionMatrix: '', features: [] },
        () => {
          ipcRenderer.send('classify-image', { data: image.path });

          ipcRenderer.on('python-events', (event: any, args: any) => {
            if (this.isJson(args)) {
              let json = JSON.parse(args);

              if (Object.keys(json)[0] === 'features') {
                console.log('mostra as features ao lado -->', json.features);
                _this.setState({ loading: false, features: json.features });
              }
            } else {
              _this.setState({ loading: false });
            }
          });
        }
      );
    }
  };

  isJson = (str: string) => {
    try {
      JSON.parse(str);
    } catch (error) {
      return false;
    }

    return true;
  };

  public render() {
    const { image, loading, confusionMatrix, features } = this.state;
    return (
      <ContentWrapper>
        <LeftContent>
          <ImageSelector changeImage={this.handleImage} />
          {image ? (
            <Btn onClick={() => this.classifyAction()}>Classificar</Btn>
          ) : (
            <DisableBtn>Classificar</DisableBtn>
          )}
        </LeftContent>
        <RightContent>
          <Feature data={features} />
          {loading && !confusionMatrix ? (
            <MessageInfo>Processando imagem...</MessageInfo>
          ) : (
            <Image src={confusionMatrix} />
          )}
        </RightContent>
      </ContentWrapper>
    );
  }
}
