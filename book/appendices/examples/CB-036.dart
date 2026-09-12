enum SyncState { local, pending, syncing, synced, conflict, failed }

Future<void> enqueueUpdate(LocalFeature f) async {
  await db.transaction(() async {
    await features.save(f.copyWith(syncState: SyncState.pending));
    await queue.insert(SyncOperation.fromFeature(f));
  });
}
