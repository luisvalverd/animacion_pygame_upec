from controller.firework_controller import FireworkAnimation  # type: ignore


def createFireworkAnimation(fireworks, waiting_time, screen):
  firework_animation = FireworkAnimation(fireworks, waiting_time, screen)
  firework_animation.setTimeAnimation(waiting_time)
  return firework_animation

