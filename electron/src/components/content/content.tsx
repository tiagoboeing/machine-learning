import * as React from "react";
import Feature from "../feature";
import ImageSelector from "../image-selector/image-selector";
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
    image?: { path?: string; preview?: any };
    confusionMatrix?: string;
    features?: [];
    loading: boolean;
    loadingClassify: boolean;
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
                    "python-training",
                    (event: any, args: any) => {
                        this.state.ipcRenderer.send("done-training", true);
                        if (this.isJson(args)) {
                            let jsonData = JSON.parse(args);

                            if (Object.keys(jsonData)[0] === "uri") {
                                console.log("matrix de confusão " + jsonData.uri);
                                this.setState({
                                    loading: false,
                                    confusionMatrix: jsonData.uri,
                                });
                            }
                        }
                    }
                );

                this.state.ipcRenderer.on("python-events", (event: any, args: any) => {
                    if (this.isJson(args)) {
                        let json = JSON.parse(args);
                        console.log("Obtained features", json);

                        if (json.features && json.prediction)
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

    handleImage = (image: object) => {
        console.log("SELECTED-IMAGE", image);
        this.setState({ image });
    };

    classifyAction = () => {
        const { ipcRenderer, image } = this.state;

        if (typeof image == "object") {
            this.setState({ loadingClassify: true }, () => {
                ipcRenderer.send("classify-image", { data: image.path });
            });
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
            image,
            loading,
            loadingClassify,
            confusionMatrix,
            features,
        } = this.state;
        return (
            <ContentWrapper>
                <LeftContent>
                    <ImageSelector changeImage={this.handleImage} />
                    {image ? (
                        !loadingClassify ? (
                            <Btn onClick={() => this.classifyAction()}>Classificar</Btn>
                        ) : (
                                <DisableBtn>Processando Imagem...</DisableBtn>
                            )
                    ) : (
                            <DisableBtn>Selecione uma imagem</DisableBtn>
                        )}
                </LeftContent>
                <RightContent>
                    <Feature data={features} />
                    {confusionMatrix ? (
                        <ImageMatrix src={confusionMatrix} />
                    ) : loading ? (
                        <MessageInfo>Realizando treinamento...</MessageInfo>
                    ) : (
                                <MessageInfo>Aguardando Treinamento</MessageInfo>
                            )}
                </RightContent>
            </ContentWrapper>
        );
    }
}
