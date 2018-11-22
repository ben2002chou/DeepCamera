# -*- mode: python -*-

block_cipher = None


a = Analysis(['../src/face_detection/worker.py'],
             pathex=['../src/face_detection'],
             binaries=[],
             datas=[],
             hiddenimports=['django', 'celery', 'celery.loaders.app', 'celery.app.amqp', 'pywt._extensions._cwt',
             'celery.fixups.django', 'celery.bin.celery', 'kombu.transport.redis', 'celery.backends',
             'celery.apps', 'celery.apps.worker', 'celery.events', 'celery.worker', 'celery.bin',
             'celery.concurrency', 'celery.contrib', 'celery.fixups', 'celery.security', 'celery.task',
             'celery.utils', 'celery.backends.redis', 'celery.app.events', 'celery.app.base.log_cls',
             'celery.app.control', 'celery.app.log', 'celery.app.control', 'celery.app.task',
             'celery.concurrency.prefork', 'celery.concurrency.eventlet', 'celery.concurrency.gevent',
             'celery.concurrency.solo', 'celery.worker.components', 'celery.worker.autoscale',
             'celery.worker.consumer', 'celery.worker.state', 'celery.worker.state.task_reserved',
             'celery.worker.state.maybe_shutdown', 'celery.worker.state.reserved_requests',
             'celery.worker.control', 'celery.worker.loops', 'celery.worker.request',
             'celery.worker.strategy', 'celery.worker.heartbeat', 'celery.worker.pidbox', 'celery.events.state'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='worker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='worker')