import cv2
import mediapipe as mp
import argparse
import os
from tqdm import tqdm

def annotate(image, results, mp_holistic, mp_drawing, mp_drawing_styles):
    annotated_image = image.copy()
    mp_drawing.draw_landmarks(annotated_image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(annotated_image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_holistic.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.
        get_default_pose_landmarks_style())
    mp_drawing.draw_landmarks(annotated_image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
    a
    return annotated_image

def video_process(args, video_name, mp_holistic,mp_face_mesh, mp_hands, mp_drawing, mp_drawing_styles,):
    video_path = os.path.join(args.video_dir, video_name)
    video = cv2.VideoCapture(video_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    heigth= int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_name = os.path.join(args.save_dir, video_name)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fnum = video.get(cv2.CAP_PROP_FRAME_COUNT)
    writer = cv2.VideoWriter(output_name, fmt, fps, (width, heigth))
    with tqdm() as pbar:
        while True:
            ret, frame = video.read()
            if ret is False:
                break
            
            with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
                results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                if results.pose_landmarks is not None:
                    frame = annotate(frame, results, mp_holistic, mp_drawing, mp_drawing_styles)
            

            writer.write(frame)
            pbar.update(1/fnum)
            # count+=1

    writer.release()
    video.release()
            


def main(args):
    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)
    videos = os.listdir(args.video_dir)
    mp_holistic = mp.solutions.holistic
    mp_face_mesh = mp.solutions.face_mesh
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils 
    mp_drawing_styles = mp.solutions.drawing_styles
    for video in tqdm(videos):
        video_process(args, video, mp_holistic, mp_face_mesh, mp_hands, mp_drawing, mp_drawing_styles,)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_dir', default='/mnt/nas3/dataset/human/upper-body/video/neet-tokyo')
    parser.add_argument('--save_dir', )
    parser.add_argument('--set_frame', help='連続何フレームのデータにするか')
    parser.add_argument('--ignore_frame', help='連続何フレームまで何も入っていないのを許容するか')
    
    args = parser.parse_args()
    main(args)