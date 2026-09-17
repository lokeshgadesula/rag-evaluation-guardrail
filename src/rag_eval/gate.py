class GateFailed(RuntimeError): pass
def enforce(summary,threshold=.85):
    if summary["faithfulness"] < threshold:
        raise GateFailed(f'faithfulness {summary["faithfulness"]:.3f} < required {threshold:.3f}')
