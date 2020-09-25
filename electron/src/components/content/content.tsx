import * as React from 'react';
import { ContentWrapper, LeftContent, RightContent } from './style';


export interface IContentProps {
}

export default class Content extends React.Component<IContentProps> {

    public render() {
        return (
            <ContentWrapper>
                <LeftContent></LeftContent>
                <RightContent></RightContent>
            </ContentWrapper>
        );
    }
}
