import styled from "styled-components";

export const ImageWrapper = styled.aside`
  display: block;
  width: 92%;
  margin: 40px auto 0px auto;
  color: #2ecc71;
  text-transform: uppercase;
  text-align: center;
  font-size: 14px;
  border-radius: 8px;

  .dropzone {
    width: 100%;
    padding: 20px;
    border: 1px dashed #2ecc71;
    cursor: pointer;
  }
`;

export const ThumbsContainer = styled.div`
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin-top: 16;
`;

export const Thumb = styled.div`
  display: inline-flex;
  width: 100%;
  max-width: 500px;
  max-width: 100%;
  height: 100%;
  margin-top: 20px;
  text-align: center;
`;

export const ThumbInner = styled.div`
  display: block;
  min-width: 100%;
  overflow: hidden;
  p{
    display:block;
    clear:both;
    width:100%;
  }
`;

export const AudioStyle = styled.audio`
  display: block;
  height: 28px;
  width: 100%;
  border-radius:4px;
  margin: 10px auto;
  text-align: center;
  border: 1px solid #2ecc71;
  background: #ffffff;
  transition: all 0.2s ease-in-out;
`;
