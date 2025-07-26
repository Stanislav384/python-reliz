def _load_animation_frames(self, folder_name, width, height):
        """Вспомогательная функция для загрузки кадров анимации из указанной папки."""
        right_frames = []
        left_frames = []
        path = os.path.join("data", folder_name)

        if not os.path.exists(path):
            print(f"Error: Animation folder '{path}' not found.")
            return

        # Получаем список файлов, сортируем их для правильного порядка
        image_files = sorted([f for f in os.listdir(path) if f.endswith(".png")])

        if not image_files:
            print(f"Warning: No image files found in '{path}'.")
            return

        for filename in image_files:
            try:
                img_path = os.path.join(path, filename)
                img_right = pygame.image.load(img_path).convert_alpha() # .convert_alpha() для прозрачности
                img_right = pygame.transform.scale(img_right, (width, height))
                right_frames.append(img_right)
                left_frames.append(pygame.transform.flip(img_right, True, False))
            except pygame.error as e:
                print(f"Error loading image {img_path}: {e}")

        self.animations_right[folder_name] = right_frames
        self.animations_left[folder_name] = left_frames

    def set_animation_state(self, state_name):
        """Устанавливает текущий набор анимационных кадров."""
        if state_name in self.animations_right and state_name in self.animations_left:
            self.current_animation_set_right = self.animations_right[state_name]
            self.current_animation_set_left = self.animations_left[state_name]
            self.current_frame_index = 0 # Сбрасываем индекс при смене анимации
            self.animation_counter = 0 # Сбрасываем счетчик
        else:
            print(f"Error: Animation state '{state_name}' not found.")
            # Fallback to idle if specified state is missing
            if "player_idle" in self.animations_right:
                self.current_animation_set_right = self.animations_right["player_idle"]
                self.current_animation_set_left = self.animations_left["player_idle"]
            else:
                self.current_animation_set_right = []
                self.current_animation_set_left = []  
