#include <msp430g2553.h>
/**
* Constants
*/
// Actions
#define R 0
#define Y 1
#define RY 2
#define G 3

// IDs of the semaphores
#define S1 (0)
#define S2 (1)
#define P1 (2)
#define P2 (3)
#define CL (4)

// Port 1.x
#define __S1L   (BIT0)
// uart 1.1     BIT1
// uart 1.2     BIT2
#define __S1H   (BIT3)
#define __S2L   (BIT4)
#define __S2H   (BIT5)
#define __SP1   (BIT6)
#define __SP2   (BIT7)

// Port 2.x
#define __ES1   (BIT0)
#define __ES2   (BIT1)
#define __ESP1  (BIT2)
#define __ESP2  (BIT3)
#define __CL1   (BIT4)

/**
* Global Variables
*/


/**
* Initialization of the system.
*
* @return void
*/
void _enable_semaphore( unsigned int, unsigned int );
void _initiate()
{
    P1DIR = __S1L + __S1H + __S2L + __S2H + __SP1 + __SP2;
    P2DIR = __ES1 + __ES2 + __ESP1 + __ESP2 + __CL1;
    P1OUT = 0;
    P2OUT = 0;
    _enable_semaphore(S1, 0);
    _enable_semaphore(S2, 0);
    _enable_semaphore(P1, 0);
    _enable_semaphore(P2, 0);
}

/**
*   Gets enable bit position in DIR register for specified semaphore.
*
* @param char semID  ID of the semaphore.
* @return char       Enable bit position in DIR register.
*/
unsigned int _get_enable_bit_position( unsigned int semID )
{
    switch( semID )
    {
    case 0: return __ES1;  break;
    case 1: return __ES2;  break;
    case 2: return __ESP1; break;
    case 3: return __ESP2; break;
    case 4: return __CL1;  break;
    }
}

/**
* Sets OUT register based on specified action.
*
* @param uint action  ID of the wanted action.
* @param uint h       Highest bit for semaphore.
* @param uint l       Lowest bit for semaphore.
* @return void
*/
void _set_bits_for_vehicles( unsigned int action, unsigned int h, unsigned int l )
{
    switch( action )
    {
    //  RED
    case R:
        P1OUT |= h + l;
        break;

    // YELLOW
    case Y:
        P1OUT |= h;
        P1OUT &= ~l;
        break;

    // RED + YELLOW
    case RY:
        // Reset high & low bit
        P1OUT &= ~h;
        P1OUT &= ~l;
        break;

    // GREEN
    case G:
	P1OUT &= ~h;
        P1OUT |= l;
        break;
    };
}

/**
* Retrives code for msp based on hardware combination operation
*
* @param char semaphore  ID of the semaphore.
* @param char opcode     1-byte opcode.
* @param uint            Number of the action.
*/
unsigned int _get_action_code( char semaphore, char opcode )
{
    if ( semaphore <= 1 )   // Vehicle semaphore
    {
        switch( opcode )
        {
        case 3: return R;  break;    // 0b11
        case 2: return Y;  break;    // 0b10
        case 1: return G;  break;    // 0b01
        case 0: return RY; break;    // 0b00
        };
    } else // Passenger & Condition semaphore
    {
        switch( opcode )
        {
        case 0: return R; break;    // Red
        case 1: return G; break;    // Green
        };
    };
}

/**
* Gets code based on specified action.
*
* @param uint action  ID of the specified action.
* @param uint m       Bit for modification.
* @return void
*/
void _set_bits_for_passengers( unsigned int action, unsigned int m )
{
    switch( action )
    {
    // RED
    case R:
        P1OUT &= ~m;
        break;

    // GREEN
    case G:
        P1OUT |= m;
        break;
    };
};

/**
* Enable/Disable semaphore by ID.
*  NOTE:
*  Enable signal is active low, that's why we are sending inverted
*  value of 'activate' variable.
*
* @param uint semID    ID of the semaphore.
* @param char activate Boolean indicator of the semaphore active state.
* @return void
*/
void _enable_semaphore( unsigned int semID, unsigned int activate )
{
    unsigned int position = _get_enable_bit_position( semID );

    // Deactivate|Activate semaphore
    if ( activate == 0 )
        P2OUT |= position;
    else
        P2OUT &= ~position;
}

/**
* Changes lights on the semaphore
*
* @param uint semID     ID of the semaphore.
* @param uint action    ID of the performable action.
    @value 0 - RED
    @value 1 - YELLOW
    @value 2 - RED + YELLOW
    @value 3 - GREEN
* @return void
*/
void _change_lights( unsigned int semID, unsigned int action )
{
    // Security check
    if ( action >= 4 || semID > 4 ) return;

    // Get semaphore & perform sepcified action.
    switch( semID )
    {
    // Semaphore S1
    case 0:
        _set_bits_for_vehicles( action, (unsigned int)__S1H, (unsigned int)__S1L );
        break;

    // Semaphore S2
    case 1:
        _set_bits_for_vehicles( action, (unsigned int)__S2H, (unsigned int)__S2L );
        break;

    // Semaphore for passengers SP1
    case 2:
        _set_bits_for_passengers( action, (unsigned int)__SP1 );
        break;

    // Semaphore for passengers SP2
    case 3:
        _set_bits_for_passengers( action, (unsigned int)__SP2 );
        break;

    // Condition light
    case 4:
        _enable_semaphore( semID, action );
        break;
    };

    // Enable semaphore
    // (in case semaphore has been previously disabled)
    if ( semID < 4 )
        _enable_semaphore( semID, 1 );
}

/**
* Parse string given from the computer (via UART).
*
* @param char second  Second received byte.
* @param char first   First received  byte.
* @return void
*/
void _parse_rdx( char second, char first )
{
    char temp = first, param;

    // Parse code for semaphore S1
    // Check enable/disable bit
    temp >>= 6;
    temp &= 1;
    if ( temp == 0 )
        _enable_semaphore( S1, 0 );
    else
    {
        temp = first & 3;
        _change_lights( S1, _get_action_code( S1, temp ) );
    };

    // Parse code for semaphore S2
    // Check enable/disable bit
    temp = (first >> 7) & 1;
    if ( temp == 0 )
        _enable_semaphore( S2, 0 );
    else
    {
        temp = (first >> 2) & 3;
        _change_lights( S2, _get_action_code( S2, temp ) );
    };



    // Parse code for passenger semaphore SP1
    // Check enable/disable bit
    temp = second & 1;
    if ( temp == 0 )
        _enable_semaphore( P1, 0 );
    else
    {
        temp = (first >> 4) & 1;
        _change_lights( P1, _get_action_code( P1, temp ) );
    }

    // Parse code for passenger semaphore SP2
    // Check enable/disable bit
    temp = (second >> 1) & 1;
    if ( temp == 0 )
        _enable_semaphore( P2, 0 );
    else
    {
        temp = (first >> 5) & 1;
        _change_lights( P2, _get_action_code( P2, temp ) );
    };

    // Condition light
    temp = (second >> 2) & 1;
    _change_lights( CL, _get_action_code( CL, temp ) );

};
