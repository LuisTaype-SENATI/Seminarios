# detector_emociones2.spec

# -*- mode: python -*-

block_cipher = None

a = Analysis(
    ['detector_emociones2.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('haarcascade_frontalface_default.xml', '.'),
        # ('modelo_emociones.h5', '.'),  # descomenta si tienes modelo
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='detector_emociones2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='detector_emociones2',
)
