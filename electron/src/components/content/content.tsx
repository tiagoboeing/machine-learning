import * as React from 'react';
import Feature from '../feature';
import ImageSelector from '../image-selector/image-selector';
import { ContentWrapper, LeftContent, RightContent, Btn, DisableBtn } from './style';

export interface IContentProps { }

export interface IContentState {
    ipcRenderer: any
    image?: object
}

export default class Content extends React.Component<IContentProps, IContentState> {
    constructor(props: IContentProps) {
        super(props);
        this.state = {
            ipcRenderer: null,
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
        this.setState({ ipcRenderer: window.require('electron').ipcRenderer });
    };

    handleImage = (image: object) => {
        console.log("SELECTED-IMAGE", image);
        this.setState({ image: image });

    }

    classifyAction = () => {
        const { ipcRenderer, image } = this.state;
        if (typeof image == 'object') {
            ipcRenderer.send('classify-image', JSON.stringify({ path: image.path, preview: image.preview }));
        }
    }

    public render() {
        const { image } = this.state;
        return (
            <ContentWrapper>
                <LeftContent>
                    <ImageSelector changeImage={this.handleImage} />
                    {image ?
                        <Btn onClick={() => this.classifyAction()} >Classificar</Btn>
                        :
                        <DisableBtn >Classificar</DisableBtn>
                    }
                </LeftContent>
                <RightContent>
                    <Feature />
                </RightContent>
            </ContentWrapper>
        );
    }
}
