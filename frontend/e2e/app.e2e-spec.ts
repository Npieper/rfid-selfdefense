import { SelfdefensePage } from './app.po';

describe('selfdefense App', function() {
  let page: SelfdefensePage;

  beforeEach(() => {
    page = new SelfdefensePage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
