def log(summary,artifacts):
    try: import mlflow
    except ImportError as e: raise RuntimeError('Install with: pip install -e ".[mlflow]"') from e
    with mlflow.start_run():
        for k,v in summary.items(): mlflow.log_metric(k,v)
        for p in artifacts: mlflow.log_artifact(str(p))
