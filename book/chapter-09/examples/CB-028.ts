type AssetUiState = {
  selectedId?: string;
  filters: { status?: string; zoneId?: string };
  loading: boolean;
  error?: string;
};
