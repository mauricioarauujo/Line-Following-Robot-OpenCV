import cv2

from funcoes import TrataImagem

def teste_img(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (320, 240))
    Direcao,QtdeLinhas = TrataImagem(img)
    info_direcao = "Direcao : " + str(Direcao)
    info_linhas = "Quantidade de Linhas : " + str(QtdeLinhas)

    cv2.putText(img, info_direcao, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.putText(img, info_linhas, (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)


    cv2.imshow("imagem", img)
    cv2.waitKey()

    print(Direcao,"  ", QtdeLinhas)


def teste_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()

        if ret:
            frame = cv2.resize(frame, (320, 240))
            Direcao, QtdeLinhas = TrataImagem(frame)
            info_direcao = "Direcao : " + str(Direcao)
            info_linhas = "Quantidade de Linhas : " + str(QtdeLinhas)

            cv2.putText(frame, info_direcao, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
            cv2.putText(frame, info_linhas, (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)


        cv2.imshow("Frame",frame)

        if cv2.waitKey(40)&0xFF == ord('q'):
            break


if __name__ == '__main__':
    #teste_img('img_video2.png')
    teste_video("Video.mp4")
