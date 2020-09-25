import styled from 'styled-components';

export const HeaderWrapper = styled.div`
    display:flex;
    justify-content:space-between;
    align-content:top;
    height:40px;    
    padding:4px 6px 0px 6px;
    width:100%;
    color:#61dafb;
    background-color:#282c34;
    border-bottom: 1px solid #61dafb;
    -webkit-touch-callout: none;
    -webkit-user-select: none; 
     -khtml-user-select: none; 
       -moz-user-select: none; 
        -ms-user-select: none; 
            user-select: none;
`;

export const GroupButtons = styled.div`
    display:flex;
    width:200px;
    justify-content:space-around;

`

export const NavButton = styled.div`
    display:block;
    font-weight:500;
    padding:4px 10px;
    line-height:26px;
    font-size:13px;
    color:#61dafb;
    cursor:pointer;
    transition: all 0.2s ease-in-out;
    border-radius:4px 4px 0px 0px;
    text-transform:uppercase;

    &:hover{
        background-color:#61dafb;
        color: #282c34;

        /* SVG HOVER COLOR */
        svg > g{
            fill: #282c34;
        }
    }
`;