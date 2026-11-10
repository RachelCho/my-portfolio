"""홈 Hero 배경 영상과 포스터를 만든다 (2026-11-10).

원본: 저장소 루트의 1110.mov (사용자 제공, 1916×1080 · 30fps · 4.6초)
- assets/video/hero-loop.mp4      데스크톱용 1916×1080, H.264, 무음(오디오 트랙 제거), faststart
- assets/video/hero-loop-960.mp4  900px 이하용 960×540
- assets/images/home-hero-video-poster-<960|1916>.jpg  첫 프레임(영상이 켜지기 전·움직임 줄이기 때 보이는 정지 화면)
어둡게 하는 처리는 영상 파일이 아니라 CSS 음영(.sc-hero--full .sc-hero-media::after)에서 한다.

실행: python3 tools/make_hero_video.py .
ffmpeg가 PATH에 없으면 imageio-ffmpeg 패키지의 ffmpeg를 쓴다.
"""
import shutil
import subprocess
import sys
from pathlib import Path


def ffmpeg_exe():
    exe = shutil.which('ffmpeg')
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit('ffmpeg가 필요합니다: brew install ffmpeg 또는 pip install imageio-ffmpeg')


def run(*args):
    subprocess.run([ffmpeg_exe(), '-v', 'error', '-y', *args], check=True)


def main(root):
    root = Path(root)
    src = root / '1110.mov'
    video = root / 'assets' / 'video'
    images = root / 'assets' / 'images'
    video.mkdir(parents=True, exist_ok=True)

    common = ['-an', '-c:v', 'libx264', '-preset', 'slow', '-profile:v', 'high',
              '-pix_fmt', 'yuv420p', '-movflags', '+faststart']
    run('-i', str(src), *common, '-crf', '23', str(video / 'hero-loop.mp4'))
    run('-i', str(src), '-vf', 'scale=960:-2', *common, '-crf', '25', str(video / 'hero-loop-960.mp4'))

    for w in (960, 1916):
        run('-i', str(src), '-frames:v', '1', '-vf', f'scale={w}:-2', '-q:v', '3',
            str(images / f'home-hero-video-poster-{w}.jpg'))

    for p in sorted(video.glob('hero-loop*.mp4')):
        print(p.relative_to(root), f'{p.stat().st_size / 1e6:.2f} MB')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
