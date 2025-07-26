 def apply_gravity(self):
        # Добавляем гравитацию
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Проверка, чтобы персонаж не ушёл ниже земли
        if self.rect.y >= GROUND_Y:
            self.rect.y = GROUND_Y
            self.velocity_y = 0
            if self.isJumping: # Если приземлились после прыжка
                self.isJumping = False
                self.set_animation_state("player_idle") # Или "player_walk" если сразу двигаемся
            self.is_falling = False
        elif self.velocity_y > 0 and not self.isJumping: # Если падаем, но не в результате прыжка
            self.is_falling = True
            self.isJumping = False # Убедимся, что isJumping False, если это падение

    def jump(self):
        # Прыжок
        if not self.isJumping and not self.is_falling: # Можем прыгать только если не прыгаем и не падаем
            self.velocity_y = JUMP_POWER
            self.isJumping = True
            self.set_animation_state("player_jump") # Активируем анимацию прыжка

    def update_animation(self):
        """Обновляет текущий кадр анимации на основе состояния персонажа."""
        # Выбираем правильный набор кадров (влево или вправо)
        current_animation_set = []
        if self.facing_right:
            current_animation_set = self.current_animation_set_right
        else:
            current_animation_set = self.current_animation_set_left

        if not current_animation_set: # Если нет кадров для текущей анимации
            return

        # Логика для выбора анимации
        if self.isJumping or self.is_falling:
            # Анимация прыжка/падения
            self.set_animation_state("player_jump") # Используем jump анимацию для прыжка и падения
            current_animation_set = self.animations_right["player_jump"] if self.facing_right else self.animations_left["player_jump"]
            # Для прыжка/падения часто используют один или несколько фиксированных кадров.
            # Здесь мы можем просто показать первый кадр прыжка или последний.
            # Если у вас несколько кадров прыжка, вы можете анимировать их так же, как ходьбу.
            if self.current_frame_index >= len(current_animation_set):
                self.current_frame_index = len(current_animation_set) - 1 # Остаемся на последнем кадре
            self.image = current_animation_set[self.current_frame_index]
        elif self.is_moving:
            # Анимация ходьбы
            if self.current_animation_set_right != self.animations_right["player_walk"]: # Избегаем постоянной переустановки
                self.set_animation_state("player_walk")
            
            current_animation_set = self.animations_right["player_walk"] if self.facing_right else self.animations_left["player_walk"]
            self.animation_counter += self.animation_speed
            if self.animation_counter >= len(current_animation_set):
                self.animation_counter = 0 # Зацикливаем анимацию
            self.current_frame_index = int(self.animation_counter)
            self.image = current_animation_set[self.current_frame_index]
        else:
            # Анимация стояния (idle)
            if self.current_animation_set_right != self.animations_right["player_idle"]: # Избегаем постоянной переустановки
                self.set_animation_state("player_idle")

            current_animation_set = self.animations_right["player_idle"] if self.facing_right else self.animations_left["player_idle"]
            self.animation_counter += self.animation_speed
            if self.animation_counter >= len(current_animation_set):
                self.animation_counter = 0 # Зацикливаем анимацию
            self.current_frame_index = int(self.animation_counter)
            self.image = current_animation_set[self.current_frame_index]

        # Обновляем изображение на основе выбранного кадра
        # Этот блок нужен, чтобы убедиться, что image всегда актуален
        if current_animation_set:
            self.image = current_animation_set[self.current_frame_index]
        else:
            self.image = pygame.Surface((self.rect.width, self.rect.height))
            self.image.fill((255, 0, 255)) # Заглушка
