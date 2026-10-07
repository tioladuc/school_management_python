
class Authorization:
    def getNameUrl(self, request)-> str:
        return request.path
    
    def urlAuthorization(self, request, pageName: str | None = None)-> bool :
        if pageName is None:
            pageName = self.getNameUrl(request)

        if(pageName == "autosication"):
            return True #request.session["user_data"].dsdd.Contain()

        return True


