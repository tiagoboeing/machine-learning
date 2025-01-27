import styled from "styled-components";

export const ContentWrapper = styled.div`
  display: flex;
  padding-top: 20px;
  padding-bottom: 30px;
  justify-content: center;
  margin-top: 50px;
`;

export const ColumnContent = styled.div`
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  vertical-align: middle;
  padding: 5px 12px;
  min-height: 85vmin;
  max-height: 85vmin;
  width: 50%;
`;

export const LeftContent = styled(ColumnContent)`
  border-right: 1px solid #7777;

  .traine {
    display: flex;
    width: 100%;
    text-align: center;
    color: #fff;
  }
  .parameters {
    display: flex;
    justify-content: space-evenly;
    width: 100%;
    height: 20px;
    label {
      color: #fff;
      height: 20px;
      margin: 0px;
      input {
        font-size: 14px;
        margin-left: 8px;
        background-color: #777;
        color: #fff;
        width: 70px;
        padding: 8px 10px;
        border-radius: 4px;
      }
    }
  }
`;

export const RightContent = styled(ColumnContent)``;

export const Btn = styled.button`
  display: block;
  height: 40px;
  line-height: 25px;
  border-radius: 4px;
  text-transform: uppercase;
  font-weight: 700;
  text-align: center;
  width: 40%;
  padding: 8px 12px;
  /* margin-top:15px; */
  color: #333;
  background-color: #2ecc71;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;

  &:active {
    color: #2ecc71;
    background-color: #333;
  }
`;

export const DisableBtn = styled(Btn)`
  background-color: #666;
  cursor: default;

  &:active {
    background-color: #666;
    color: #333;
  }
`;

export const MessageInfo = styled.p`
  display: block;
  width: 90%;
  height: 40px;
  padding: 10px;
  font-size: 18px;
  color: #2ecc71;
  border: 1px solid #333;
  background-color: #333;
  text-align: center;
`;

export const Image = styled.img`
  max-width: 100%;
`;

export const ImageMatrix = styled.img`
  max-width: 90%;
  margin-top: 12px;
`;
