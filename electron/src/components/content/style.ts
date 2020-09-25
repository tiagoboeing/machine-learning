import styled from 'styled-components';

export const ContentWrapper = styled.div`
    display:flex;
    padding-top:30px;
    padding-bottom:30px;
    justify-content:center;
`;

export const ColumnContent = styled.div`
    display:flex;
    min-height:85vmin;
    max-height:85vmin;
    width:50%;
`;

export const LeftContent = styled(ColumnContent)`
    border-right:1px solid #7777;
    
`;

export const RightContent = styled(ColumnContent)`
    
`;
