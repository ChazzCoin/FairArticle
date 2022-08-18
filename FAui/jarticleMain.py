from PyQt6 import QtWidgets
import sys
from FW.FairSocket import Server
from F.CLASS import Thread
from FCM.Jarticle.jProvider import jPro
from F import LIST, DICT, DATE, OS
from FQt import FairUI
from FM import MServers
from FW.FairSocket import FairMessage
from ViewElements import ViewElements
from FW.FairSocket.Client import FairClient


ui_file_path = f"{OS.get_cwd()}/jarticle.ui"

"""
 -> Everything/Widget should be named exactly the name
    : QtDesigner -> btnSearch
    : Class Variable -> btnSearch
    : Action Function -> action_btnSearch
"""

class LucasUI(FairUI, ViewElements):
    """ Variables are in ViewElements """
    searchMode = "default"
    fairclient = None

    def __init__(self):
        super(LucasUI, self).__init__()
        # -> Load UI Template File
        self.bind_ui(ui_file_path)
        # -> Do Custom Work
        self.toggleServerIsConnected.setEnabled(False)
        # # -> Finish Up
        self.show()

    """ Actions """

    def onClick_btnNext(self, item):
        if not self.current_articles:
            return
        title = self.get_dict("title", self.current_article)
        item = DICT.get_random(self.current_articles)
        newTitle = self.get_dict("title", item)
        if title == newTitle:
            item = DICT.get_random(self.current_articles)
        self.set_current_article(item)

    def onToggled_checkSummary(self, item):
        self.toggleSummary = item

    def onDoubleClick_listArticlesByTitle(self, item):
        title = item.text()
        new_article = DICT.get(title, self.current_articles)
        self.set_current_article(new_article)
        self.tabWidget.setCurrentIndex(1)

    def onTextChanged_editSearchText(self, item):
        print("onTextChanged", item)

    def onClick_btnSearch(self):
        """ Master Search """
        self._build_search()

    def _load_new_articles(self, results):
        self.set_current_articles(results)
        firstArt = LIST.get(0, results)
        self.set_current_article(firstArt)

    def _build_search(self):
        results = []
        searchTerm = self.editSearchText.text()
        todaysDate = DATE.get_now_month_day_year_str()
        earliestDate = DATE.TO_DATETIME("January 01 1900")
        limit = self.editSearchLimit.toPlainText() if self.editSearchPage.toPlainText() != "" else 10
        page = self.editSearchPage.toPlainText() if self.editSearchPage.toPlainText() != "" else 1
        rawSpecificDate = self.dateSearchSpecific.text()
        if self.searchMode == "dateRange":
            rawDateRangeBefore = self.dateRangeSearchBefore.text()
            rawDateRangeAfter = self.dateRangeSearchAfter.text()
            results = self.jpro.search_by_date_range(searchTerm=searchTerm, gte=rawDateRangeAfter, lte=rawDateRangeBefore, limit=limit)
        elif self.searchMode == "onDate":
            results = self.jpro.search_by_date_range(searchTerm=searchTerm, gte=rawSpecificDate, lte=rawSpecificDate, limit=limit)
        elif self.searchMode == "beforeDate":
            results = self.jpro.search_by_date_range(searchTerm=searchTerm, gte=earliestDate, lte=rawSpecificDate, limit=limit)
        elif self.searchMode == "afterDate":
            results = self.jpro.search_by_date_range(searchTerm=searchTerm, gte=rawSpecificDate, lte=todaysDate, limit=limit)

        self._load_new_articles(results)

    def onClick_btnChatConnect(self, item):
        host = self.editChatHost.text()
        self.fairclient = FairClient(host=host, userName="Jarticle", callback=self.onOverrideMessage)
        self.fairclient.connect()
        self.fairclient.emitOnConnect()
        self.toggleChatIsConnected.setChecked(True)
        self.toggleChatIsConnected.setEnabled(False)

    def onClick_btnChatSend(self, item):
        mess = self.editChatInput.text()
        m = f"ME: {mess}"
        self.listChatMessages.addItem(m)
        messObj = FairMessage(message=mess, userName=self.fairclient.userName)
        self.fairclient.emit("onMessage", messObj.toJson())
        self.editChatInput.setText("")

    def onOverrideMessage(self, data):
        print("override", data)
        fm = FairMessage().fromJson(data)
        if not fm:
            return
        if fm.userName == self.fairclient.userName:
            return
        m = f"{fm.userName}: {fm.message}"
        self.listChatMessages.addItem(m)

    def onClick_btnChatServerStart(self, item):
        Thread.runFuncInBackground(Server.FairServer().start)
        self.toggleChatServerIsRunning.setChecked(True)
        self.toggleChatServerIsRunning.setEnabled(False)

    def onToggled_toggleRangeEnable(self, item):
        self._reset_toggleDates()
        self.toggleRangeEnable.setChecked(item)
        self.searchMode = "dateRange"

    def onToggled_toggleOnDate(self, item):
        if item:
            self.__toggleOnDate(True, True)
            self.searchMode = "onDate"
            self.__toggleBeforeDate(False, False)
            self.__toggleAfterDate(False, False)
        else:
            self._reset_toggleDates()

    def onToggled_toggleBeforeDate(self, item):
        if item:
            self.__toggleOnDate(False, False)
            self.__toggleBeforeDate(True, True)
            self.searchMode = "beforeDate"
            self.__toggleAfterDate(False, False)
        else:
            self._reset_toggleDates()

    def onToggled_toggleAfterDate(self, item):
        if item:
            self.__toggleOnDate(False, False)
            self.__toggleBeforeDate(False, False)
            self.__toggleAfterDate(True, True)
            self.searchMode = "afterDate"
        else:
            self._reset_toggleDates()

    def _reset_toggleDates(self):
        self.__toggleOnDate(False, True)
        self.__toggleBeforeDate(False, True)
        self.__toggleAfterDate(False, True)

    def __toggleOnDate(self, setTrue, isEnabled=True):
        self.toggleOnDate.setEnabled(isEnabled)
        self.toggleOnDate.setChecked(setTrue)

    def __toggleBeforeDate(self, setTrue, isEnabled=True):
        self.toggleBeforeDate.setEnabled(isEnabled)
        self.toggleBeforeDate.setChecked(setTrue)

    def __toggleAfterDate(self, setTrue, isEnabled=True):
        self.toggleAfterDate.setEnabled(isEnabled)
        self.toggleAfterDate.setChecked(setTrue)

    def onClick_btnCryptoReport(self):
        pass

    def onClick_btnMetaReport(self):
        meta_articles = self.jpro.get_metaverse_articles()
        self.set_current_articles(meta_articles)
        pass

    def onClick_btnServerConnect(self):
        name = self.editServerName.text()
        host = self.editServerHost.text()
        port = self.editServerPort.text()
        dbUri = MServers.BASE_MONGO_URI(host, port)
        self.jpro = jPro(dbUri=dbUri, dbName=name)
        if self.jpro and self.jpro.is_connected():
            self.toggleServerIsConnected.setChecked(True)
            self.get_server_details()

    def onClick_btnClear(self):
        self.listArticlesByTitle.clear()
        self.lblResultCountNumber.setText("0")
        self.lblTitle.setText("...")
        self.txtBody.setText("")
        self.clearSearchText()

    """Server Details"""
    def get_server_details(self):
        self.set_article_count()

    """ Article Work """
    def set_article_count(self):
        if self.jpro:
            art_count = self.jpro.get_article_count()
            self.lblArticleCountNumber.setText(str(art_count))

    def set_current_articles(self, articles):
        if not articles:
            return
        self.listArticlesByTitle.clear()
        count = len(articles)
        self.lcdResultCount.display(int(count))
        self.lblResultCountNumber.setText(str(count))
        isFirst = True
        for art in articles:
            if isFirst:
                self.set_current_article(art)
                isFirst = False
            key = DICT.get("title", art)
            # tempDate = DICT.get("published_date", art)
            # key = f"{tempDate}.{tempTitle}"
            self.current_articles[key] = art
            self.listArticlesByTitle.addItem(key)

    def set_current_article(self, article):
        if not article:
            self.txtBody.setText("No Articles Found...")
            return
        # -> Set Global Current
        self.current_article = article
        # -> Set Title
        title = DICT.get("title", article, default="No Title...")
        self.lblTitle.setText(title)
        #
        pDate = DICT.get("published_date", article)
        self.editDetailsDatePublished.setText(pDate)
        self.editDetailsDatePublished.setEnabled(False)
        author = DICT.get("author", article)
        self.editDetailsAuthor.setText(str(author))
        self.editDetailsAuthor.setEnabled(False)
        category = DICT.get("category", article)
        self.editDetailsCategory.setText(category)
        self.editDetailsCategory.setEnabled(False)
        score = DICT.get("score", article)
        self.editDetailsScore.setText(str(score))
        self.editDetailsScore.setEnabled(False)
        source = DICT.get("source", article)
        self.editDetailsSource.setText(source)
        self.editDetailsSource.setEnabled(False)
        url = DICT.get("url", article)
        self.editDetailsUrl.setText(url)
        self.editDetailsUrl.setEnabled(False)
        # -> Set Main Body
        body = DICT.get("body", article, default="No Body...")
        if self.toggleSummary:
            summary = DICT.get("summary", article, default=False)
            self.txtBody.setText(summary if summary else body)
        else:
            self.txtBody.setText(body)

    def clearSearchText(self):
        self.editSearchText.setText("")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LucasUI()
    sys.exit(app.exec())
