def get_api_key() -> str:
    """Securely prompt for Companies House API key."""
    try:
        return getpass.getpass("Please enter your Companies House API key: ")
    except Exception as e:
        logger.error(f"Error getting API key: {e}")
        raise