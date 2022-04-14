from utils.menu import NAV_MENU


class RenderMixin:
    paginate_by = 5

    def get_render_data(self, **kwargs) -> dict:
        context = kwargs
        nav_menu = NAV_MENU.copy()
        if not self.request.user.is_authenticated:
            subscribe_page_index = 1
            nav_menu.pop(subscribe_page_index)

        context['nav_menu'] = nav_menu
        return context


class PermissionMixin:
    def get_permissions_by_action(self):
        try:
            return [permission() for permission in
                    self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
