import * as React from "react";
import Feature from "../feature";
import AudioSelector from "../image-selector/image-selector";
import {
  Btn,
  ContentWrapper,
  DisableBtn,
  ImageMatrix,
  LeftContent,
  MessageInfo,
  RightContent,
} from "./style";

export interface IContentProps { }

export interface IContentState {
  ipcRenderer: any;
  audio?: { path?: string; preview?: any };
  confusionMatrix?: string;
  features?: [];
  loading: boolean;
  loadingClassify: boolean;
  classifType: string;
  learning_rate: number;
  trainning_time: number;
  accResult: any;
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
      loadingClassify: false,
      classifType: "",
      learning_rate: 0.1,
      trainning_time: 5011,
      accResult: null,
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
        loading: false,
      },
      () => {
        this.state.ipcRenderer.on(
          "reply-done-training",
          (event: any, args: any) => {
            console.log("HEADER", args);
            this.setState({ loading: false });
          }
        );
        this.state.ipcRenderer.on(
          "python-training",
          (event: any, args: any) => {
            this.state.ipcRenderer.send("done-training", true);
            if (this.isJson(args)) {
              let jsonData = JSON.parse(args);
              if (jsonData.accuracy) {
                console.log("Resultado ", args);
                this.setState({
                  loading: false,
                  accResult: jsonData.accuracy.toFixed(3),
                });
              }
            }
          }
        );

        this.state.ipcRenderer.on("python-events", (event: any, args: any) => {
          if (this.isJson(args)) {
            let json = JSON.parse(args);
            console.log("Obtained features", json);

            if (json.result && json.features)
              this.setState({
                loadingClassify: false,
                features: json,
              });
          } else {
            this.setState({ loadingClassify: false });
          }
        });
      }
    );
  };

  handleAudio = (audio: object) => {
    console.log("SELECTED-AUDIO", audio);
    this.setState({ audio });
  };

  traineeAction = () => {
    const { ipcRenderer, learning_rate, trainning_time } = this.state;
    this.setState(
      { classifType: "Áudio", loadingClassify: false, loading: true },
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

  classifyAction = () => {
    const { ipcRenderer, audio } = this.state;

    if (typeof audio == "object") {
      this.setState(
        { classifType: "Áudio", loadingClassify: true },
        () => {
          let data = [
            'classify',
            audio.path
          ];

          ipcRenderer.send("classify-audio", { data: data });
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
    const {
      audio,
      loading,
      loadingClassify,
      features,
      classifType,
      learning_rate,
      trainning_time,
      accResult
    } = this.state;
    return (
      <ContentWrapper>
        <LeftContent>
          <div className="traine">
            {(!loading ? (
              <>
                <Btn onClick={() => this.traineeAction()}>Treinar</Btn>
              </>
            ) : (
                <DisableBtn>Treinando...</DisableBtn>
              ))}
            {accResult && <p>Treinamento concluido e obtido acurácia de <strong>{(accResult * 100).toFixed(2)}%</strong></p>}
          </div>
          <div className="parameters">

            <label>Learning Rate:
                  <input type="number" min="0.01" value={learning_rate} onChange={(e) => this.setState({ learning_rate: parseFloat(e.target.value) })} />
            </label>
            <label>Trainning Time:
                  <input type="number" min="0.01" value={trainning_time} onChange={(e) => this.setState({ trainning_time: parseFloat(e.target.value) })} />
            </label>
          </div>
          <AudioSelector changeImage={this.handleAudio} />
          {audio &&
            (!loadingClassify && !loading ? (
              <>
                <Btn onClick={() => this.classifyAction()}>Classificar</Btn>
              </>
            ) : (
                <DisableBtn>Processando Áudio...</DisableBtn>
              ))}
        </LeftContent>
        <RightContent>
          <Feature
            type={classifType}
            loadingData={loadingClassify}
            data={features}
          />
          {loading ? (
            <MessageInfo>Realizando treinamento...</MessageInfo>
          ) : null}
        </RightContent>
      </ContentWrapper>
    );
  }
}
