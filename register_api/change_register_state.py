from myapp.models.user_model import User


def change_register_state_func(user_id, new_state):
    User.save_state(state=new_state, user_id=user_id)
