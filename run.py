import sys
from YuNet import YuNet

detector = YuNet(
        model=r"models\postproc_yunet_top50_th60_360x640_sh4.blob",
        model_resolution="360x640",
        input_src=r"IRON MAN 2 (2010) .mp4",
        # resolution=args.resolution,
        stats=True,
        trace=True,
        internal_fps = 60,
        internal_frame_height = 720
        )

while True:
    # Run face detector on next frame
    frame, faces = detector.next_frame()
    print("FRAME =", frame)
    print()
    print("FACES =", faces)
