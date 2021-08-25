from . import user_bp

@user_bp.ruote('/get_user')
def get_user():
  return 'get user'