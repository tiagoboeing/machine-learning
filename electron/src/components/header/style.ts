import styled from "styled-components";

const primary = "#61dafb";

export const HeaderWrapper = styled.div`
  display: flex;
  justify-content: space-between;
  align-content: top;
  padding: 25px 20px 0px 20px;
  width: 100%;
  color: ${primary};
  background-color: #282c34;
  border-bottom: 1px solid ${primary};
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  position: fixed;
  top: 0;
  &::after {
    -webkit-app-region: drag;
    content: "";
    width: 100%;
    height: 10px;
    text-align: center;
    background: rgba(0, 0, 0, 0.4);
    position: absolute;
    top: 0px;
    left: 0;
    cursor: grab !important;
  }

  h1 {
    font-size: 1rem;
  }
`;

export const DragWindow = styled.div`
  -webkit-app-region: drag;
  &:hover {
    cursor: grab;
  }
`;

export const GroupButtons = styled.div`
  display: flex;
  justify-content: space-between;
  width: 100%;
`;

export const NavButton = styled.button`
  display: block;
  font-weight: 500;
  padding: 4px 10px;
  margin-left: 20px;
  line-height: 26px;
  font-size: 14px;
  color: ${primary};
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  border-radius: 4px 4px 0px 0px;
  /* text-transform: uppercase; */
  background: none;
  min-width: ${(props: NavButtonProps) => props.useMinWidth && "200px"};

  &:disabled {
    color: #000000;
    background: #999999;
    cursor: not-allowed;
  }
  &:last-child {
    justify-self: flex-end;
  }

  &:hover {
    background-color: ${primary};
    color: #282c34;

    /* SVG HOVER COLOR */
    svg > g {
      fill: #282c34;
    }
  }
`;

export interface NavButtonProps {
  useMinWidth?: boolean;
}
