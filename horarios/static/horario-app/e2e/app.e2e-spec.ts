import { HorarioPage } from './app.po';

describe('horario App', function() {
  let page: HorarioPage;

  beforeEach(() => {
    page = new HorarioPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
