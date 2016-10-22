import { HorarioAppPage } from './app.po';

describe('horario-app App', function() {
  let page: HorarioAppPage;

  beforeEach(() => {
    page = new HorarioAppPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
