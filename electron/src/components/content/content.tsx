import * as React from 'react';
import Feature from '../Feature';

import { ContentWrapper, LeftContent, RightContent } from './style';

export interface IContentProps {}

export default class Content extends React.Component<IContentProps> {
  public render() {
    return (
      <ContentWrapper>
        <LeftContent></LeftContent>
        <RightContent>
          <Feature />
        </RightContent>
      </ContentWrapper>
    );
  }
}
