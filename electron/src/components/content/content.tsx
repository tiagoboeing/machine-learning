import * as React from 'react';
import ImageSelector from '../image-selector/image-selector';
import { ContentWrapper, LeftContent, RightContent, Btn} from './style';


export interface IContentProps {
}

export default class Content extends React.Component<IContentProps> {

    public render() {
        return (
            <ContentWrapper>
                <LeftContent>
                    <ImageSelector />
                    <Btn>Classificar</Btn>
                </LeftContent>
                <RightContent></RightContent>
            </ContentWrapper>
        );
    }
}
